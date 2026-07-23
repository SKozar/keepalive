class Keepalive < Formula
  desc "Keep macOS awake for Teams during chosen hours"
  homepage "https://github.com/skozar/keepalive"
  version "0.5.2"
  url "https://github.com/skozar/keepalive/releases/download/v#{version}/keepalive-#{version}.tar.gz"
  sha256 "3d6181cebdc8907e12a2c1d734da1d0ff4817552dc978638e3d9cb393a7a3e0c"

  def install
    libexec.install Dir["*"]
    bin.install_symlink libexec/"keepalive"
  end

  def caveats
    <<~EOS
      To start the agent:
        keepalive start

      To run with custom schedule:
        keepalive start --schedule 04:00-12:00 --idle 180

      Logs: ~/Library/Logs/keepalive/keepalive.log

      IMPORTANT: Grant Accessibility permission to keepalive:
        System Settings → Privacy & Security → Accessibility
        Add: #{opt_bin}/keepalive
    EOS
  end
end
